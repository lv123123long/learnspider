import requests

headers = {
    'Cookie': '_octo=GH1.1.523860061.1648366268; tz=Asia%2FShanghai; _device_id=e1df4f974c9304e5b7a1c801b545bfbc; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; user_session=a4HxKQgsMsW6YOmAVxCMjBg_c6ISN1jFWLs7bZu6ieRxdwty; __Host-user_session_same_site=a4HxKQgsMsW6YOmAVxCMjBg_c6ISN1jFWLs7bZu6ieRxdwty; logged_in=yes; dotcom_user=lv123123long; preferred_color_mode=light; has_recent_activity=1; _gh_sess=PnEf1H5z%2BwQ7hhMGk7XE8C6DRPlCYSOvqE3kblXosJ46DlImOZOBfC9eKwbog%2FAkL52MXM8niSkAdAscDHxh6gAkPSSiJBo1FbRPFMWp1BIx9%2BCMOk6RSfp791iNkJ3rTgntqC%2FLFj%2Bs9zGp0tF0W%2FbN2opQMd2OYPIfdLboxft8o4DGn2lhUw6%2BQoOyvfNShIs9fHXouKaTjABd%2BiNRp340UrKTSHcciH8ah4D5UZ7UAoZPIrw5o0X3CkaxkqDdw0s0Ycnt3Ja6s9NKiNQJ5EfNOAeY1kYprcm4IiCTm0DWZS9rD73FYb9RK%2BsibXlzGvF%2BDxZkGF%2FSA0dixCblStsdaKdJfn95jyNtCzmFkVGLWSgxXYzAIrOW3osVCUrRhbvR1THogryN75%2BsHwagcag%2F7CskhrdgQmdpZNtLvByoj%2F1ZKQ4hGYdbTNyuBl0g--0SDbWKBY7CBqJWQP--Hp1zL2s9ULtvCG%2BVXZK3TQ%3D%3D'

}

r = requests.get('https://github.com/', headers = headers)
print(r.text)