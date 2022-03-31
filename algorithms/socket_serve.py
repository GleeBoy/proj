import socket
import os
import socketserver
import threading
from PIL import Image
import queue
import time
from gateManage.models import *
import json
import logging
from multiprocessing import Process


def cfg_data():
    cfg = AppConfig.objects.all()[0]
    data = {"app_led_brightness": cfg.app_led_brightness, "app_ir_brightness": cfg.app_ir_brightness,
            "app_led_time": cfg.app_led_time, "app_confidenceLevel": int(cfg.app_confidenceLevel * 100),
            "app_backlight_standby": cfg.app_backlight_standby, "app_switch_time": cfg.app_switch_time,
            "app_face_live": int(cfg.app_face_live), "app_face_box_val": cfg.app_face_box_val,
            "app_mask": int(cfg.app_mask), "app_temperature_switch": int(cfg.app_temperature_switch),
            "app_temperature_limit": int(cfg.app_temperature_limit * 100), "app_temp_warn": int(cfg.app_temp_warn),
            "app_volume": cfg.app_volume}
    return data


def org_stru(source_id, target_id, cmd, str_data):
    head = 'AABBCCDDEE'
    if isinstance(str_data, str):
        data = str_data.encode()
    else:
        data = str_data
    # size = (hex(len(data))[2:]).ljust(8, '0')
    size = (len(data)).to_bytes(4, byteorder='little')
    data_1 = bytes.fromhex(head + source_id + target_id + cmd)
    data = data_1 + size + data
    xor_value = 0
    for item in data:
        xor_value ^= item
    # xor_val = bytes.fromhex(hex(xor_value)[2:])
    xor_val = (xor_value).to_bytes(1, byteorder='little')
    return data + xor_val


class RequestHandler(socketserver.StreamRequestHandler):
    # CA_q = queue.Queue(5)
    QT_q = queue.Queue(5)
    SF_q = queue.Queue(5)
    WW_q = queue.Queue(5)
    pict_feature = queue.Queue(5)
    app_face_box_return = queue.Queue(5)
    ww_return = queue.Queue(5)
    actions_return = queue.Queue(2)

    def handle(self):
        # print("conn is:", self.request)  # conn,addr = sock.accept()
        try:
            raddr = self.request.getpeername()
            t5 = threading.Timer(1, self.dist_data)
            t5.start()
            # t6 = threading.Timer(1, self.test_sf_q)
            # t6.start()
            if raddr == '/userdata/socket/asf_web_client.socket':   # 发送不同数据
                while True:
                    sf_send_data = self.SF_q.get()
                    print('sf_send_data:%s' % sf_send_data)
                # send_data = self.org_stru(sf_send_data)
                    try:
                        self.request.sendall(sf_send_data)
                    except Exception as e:
                        print(e)
                        self.SF_q.put(sf_send_data)
                        break
            elif raddr == '/userdata/socket/deveice_web_client.socket':
                while True:
                    ww_send_data = self.WW_q.get()
                    print('ww_send_data:%s' % ww_send_data)
                    try:
                        self.request.sendall(ww_send_data)
                    except Exception as e:
                        self.WW_q.put(ww_send_data)
                        break
            elif raddr == '/userdata/socket/feature_client.sock':
                while True:
                    pict_feature = self.pict_feature.get()
                    try:
                        self.request.sendall(pict_feature)
                    except:
                        self.pict_feature.put(pict_feature)
                        break
            elif raddr == '/userdata/socket/cfg_client.sock':
                while True:
                    face_box = self.app_face_box_return.get()
                    # ww_r = self.ww_return.get()
                    # if face_box[12] == b'\x01'[0] and ww_r[12] == b'\x01'[0]:
                    try:
                        if face_box[12] == b'\x01'[0]:
                            self.request.sendall('1'.encode())
                        else:
                            self.request.sendall('0'.encode())
                    except:
                        self.app_face_box_return.put(face_box)
                        break
            elif raddr == '/userdata/socket/actions_client.sock':
                sf_put = org_stru('A4', 'A2', '03', '')
                self.SF_q.put(sf_put)

                face_box = self.actions_return.get()
                try:
                    self.request.sendall(face_box)
                except:
                    self.actions_return.put(face_box)

        except Exception as e:
            print(e)

    def judge_xor(self, recv_data):
        xor_value = 0
        for item in recv_data[:-1]:
            xor_value ^= item
        if xor_value == recv_data[-1]:
            return True
        else:
            return False

    def dist_data(self):
        try:
            # recv_multi_data = self.request.recv(8192)
            # print('recv_multi_data' % recv_multi_data)
            # for i in recv_multi_data.split(b'\xaa\xbb\xcc\xdd\xee'):
            #     if i:
            #         j = b'\xaa\xbb\xcc\xdd\xee' + i
            while True:
                recv_data = self.request.recv(8192)
                print('recv_data: %s' % recv_data)
                if recv_data:
                    if recv_data[0] != b'\xaa'[0]:
                        picture_stru = org_stru('A4', 'A2', '02', recv_data)
                        self.SF_q.put(picture_stru)
                        ww_stru = org_stru('A4', 'A3', 'd5', recv_data)
                        self.WW_q.put(ww_stru)
                    if self.judge_xor(recv_data):
                        if recv_data[5] == b'\xa2'[0] and recv_data[6] == b'\xa4'[0]:
                            if recv_data[7] == b'\x01'[0]:
                                if recv_data[8] == b'\x00'[0]:
                                    self.pict_feature.put(b'0')
                                else:
                                    self.pict_feature.put(recv_data[12:-1])
                            elif recv_data[7] == b'\x02'[0]:
                                self.app_face_box_return.put(recv_data)
                            elif recv_data[7] == b'\x03'[0]:
                                self.actions_return.put(recv_data)
                            elif recv_data[7] == b'\xf2'[0]:
                                data = cfg_data()
                                picture_stru = org_stru('A4', 'A2', 'f2', json.dumps(data))
                                self.SF_q.put(picture_stru)
                        elif recv_data[5] == b'\xa3'[0] and recv_data[6] == b'\xa4'[0]:
                            if recv_data[7] == b'\xd5'[0]:
                                # self.ww_return.put(recv_data)
                                pass
                            elif recv_data[7] == b'\xf3'[0]:
                                json_data = recv_data[12:-1].decode()
                                dict_data = json.loads(json_data)
                                user_id = dict_data.get('user_id')
                                user = User.objects.get(id=user_id)
                                if Record.objects.count() > 100000:
                                    r = Record.objects.all().first()
                                    Record.objects.filter(id=r.id).delete()
                                Record.objects.create(img_path=dict_data.get('img_path'), name=user.name,
                                                      department=user.department, id_card=user.id_card,
                                                      work_card=user.work_card, ic_code=user.ic_code,
                                                      user_id=user_id, animal_heat=dict_data.get('animal_heat'))
                            elif recv_data[7] == b'\xf1'[0]:
                                data = cfg_data()
                                picture_stru = org_stru('A4', 'A3', 'f1', json.dumps(data))
                                self.WW_q.put(picture_stru)
                        elif recv_data[5] == b'\xa4'[0] and recv_data[6] == b'\xa2'[0] and recv_data[7] == b'\x01'[0]:
                            self.SF_q.put(recv_data)
                    else:
                        print('异或值验证失败')
                else:
                    break
                    # if j[6] == b'\xa0':
                    #     CA_q.put(j)
                    # if j[7] == b'\xa1':
                    #     QT_q.put(j)
                    # if j[7] == b'\xa2':
                    #     SF_q.put(j)
                    # if j[7] == b'\xa3':
                    #     WW_q.put(j)
        except Exception as e:
            print(e)

    # def test_sf_q(self):
    #     while True:
    #         SF_q.put(b'\xaa\xbb\xcc\xdd\xee\xa4\xa2\x01-\x00\x00\x00/userdata/web/gate/media/uploadsIMG/gezhe.jpg\xd3')
    #         time.sleep(5)


SERVERADDR = '/userdata/socket/web_server.socket'


def start_socket_serve():
    if os.path.exists(SERVERADDR):
        os.unlink(SERVERADDR)
    # HOST, PORT = "localhost", 9999
    s = socketserver.ThreadingUnixStreamServer(SERVERADDR, RequestHandler)     # 创建了一个线程的TCP服务器类，也就是通过多线程来进行应答客户端
    s.serve_forever()


def tsss():
    # t4 = threading.Thread(target=start_socket_serve)
    # t4.start()
    p = Process(target=start_socket_serve)
    p.start()



