# from nonebot.adapters.onebot.v11 import Bot, Event, GroupRecallNoticeEvent, GROUP_MEMBER
# from nonebot.adapters.onebot.v11.message import Message
# from nonebot.plugin import export, on_notice
# from nonebot.rule import Rule
# from nonebot.typing import T_State
# from nonebot.adapters.onebot.v11 import Bot
#
# export = export()
# export.name = '防撤回小助手'
# export.usage = '你撤回一下就知道了的[]~(￣▽￣)~*'
#
# name_list = ['1196991321','308730057','1916618840','709899278']
#
# async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
#     return isinstance(event, GroupRecallNoticeEvent)
#
# recall = on_notice(priority=50,rule=Rule(_checker)) #
#
# def _func(name:str):
#     for id in name_list:
#         if str(id) == name:
#             return False
#     print(name)
#     return True
# def msg_handler(operator_id,recall_message):
#     return Message(
#         f'[CQ:at,qq={operator_id}] 撤回了消息\n——————————————\n{recall_message}'
#     )
# @recall.handle()
# async def pro(bot: Bot, event: GroupRecallNoticeEvent, state: T_State):
#     if _func(str(event.operator_id)):
#         die_mess = await bot.call_api('get_msg', **{
#             'message_id': event.message_id
#         })
#         if  '撤回了消息' in str(die_mess):
#             pass
#         else:
#             recall_message = die_mess['message']
#             await recall.send(msg_handler(event.get_user_id(),recall_message))