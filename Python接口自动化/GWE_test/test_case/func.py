
def get_auth():
    from order_service.api.service.admin_login_api import AdminLoginApi
    login_api_obj = AdminLoginApi().send_request()
    return_data = login_api_obj.resp.data
    return return_data.tokenHead + ' ' + return_data.token


auth_token = get_auth()  # 为什么放在这里就执行
