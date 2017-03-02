#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import logging;logging.basicConfig(level=logging.INFO)
import orm
from models import User

async def test():
    await orm.create_pool(loop=loop,host='127.0.0.1', port=3306, user='www-data', password='www-data', db='awesome')
    u = User(name='zhifeng yan', email='yanzhifeng@shie.com.cn', passwd='123456', image='about:blank')
    await u.save()
    logging.info('tesk ok')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

loop.close()
