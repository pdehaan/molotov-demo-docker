from molotov import scenario
@scenario(weight=100)
async def _test(session):
    async with session.get('https://fine-citadel-142015.uc.r.appspot.com/') as resp:
        assert resp.status == 200, resp.status
