card_list = []
def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1.新增明片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def add_card():
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入qq:")
    email_str = input("请输入邮箱:")
    # 2.使用用户输入名片的信息建立一个名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加 %s 成功" % name_str)
def show_all():
    print("-" * 50)
    # 打印表头
    for name in ["姓名","电话","qq","邮箱"]:
        print(name,end="\t\t")
    print("")
    # 打印分隔线
    print("=" * 50)
    # 遍历名片列表，显示全部
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["qq"],
                                      card_dict["email"]))
    # 判断是否有名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片。")
        return

def search_card():
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入需要搜索的名片:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了")
         # 打印分隔线
            print("==" * 50)
            # 打印表头
            for name in ["姓名","电话","qq","邮箱"]:
                print(name,end="\t\t")
            print("")
                # 打印找到的名片信息
            for card_dict in card_list:
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
                # 针对找到的名片记录增加修改和删除操作
                deal_card(card_dict)
                break
        else:
            print("没有找到 %s" % find_name)
def deal_card(find_dict):
    """ 处理查找到的名片

    :param find_dict:查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作"
                       "【1】修改【2】删除 【0】返回上一层")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")

        print("修改名片成功")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片")
def input_card_info(dict_value,tip_message):
    """ 输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，则返回该内容，若无，返回原内容
    """
    # 1、提示用户输入内容
    result_str = input(tip_message)
    # 2、针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3、如果用户没有输入内容，返回‘字典中原有的值’。
    else:
        return dict_value




