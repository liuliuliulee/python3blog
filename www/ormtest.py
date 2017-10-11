import orm
from models import User, Blog, Comment
import asyncio
from config import configs


async def test():
    await orm.create_pool(loop=loop, user='liuliuliulee',password='biao162911',db='blog')
    # await orm.create_pool(loop=loop, **configs.db)

    u = User(name='Tdedafastad', email='hello_world@163', passwd='d12ad31', image='addaa')

    await u.save()
    r = await User.findAll()
    await orm.close_pool()
    print(r)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()