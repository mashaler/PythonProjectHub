#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0 

import qrcode as qr

qrImg = qr.make("https://mashaler.github.io/personal_portfolio-website.github.io/")
qrImg.save('demo.png')
