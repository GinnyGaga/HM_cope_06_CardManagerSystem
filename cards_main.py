import cards_tools
while True:
    # 显示欢迎界面
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是 【%s】 " % action_str)

    # 1，2，3是针对名片的操作选择
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.add_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 搜索名片
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("退出系统，欢迎下次光临")
        break
    # 0表示退出系统
    #     pass
    else:
        print("您的选择错误，请重新选择：")