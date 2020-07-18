#!/usr/bin/env python
# coding=utf-8
import requests
src = "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&hs=2&pn=0&spn=0&di=173360&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=2534506313%2C1688529724&os=1097436471%2C408122739&simid=3354786982%2C133358663&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E5%9B%BE%E7%89%87&objurl=http%3A%2F%2Fa3.att.hudong.com%2F14%2F75%2F01300000164186121366756803686.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fp7rtwg_z%26e3Bkwthj_z%26e3Bv54AzdH3Ftrw1AzdH3Fwn_89_0c_a8naaaaa8m98bm8d8nmm0cmbanmbm_3r2_z%26e3Bip4s&gsm=1&islist=&querylist="
r = requests.get(src)
with open("./data/tieba/images/1.jpg", "wb") as file:
        file.write(r.content)
