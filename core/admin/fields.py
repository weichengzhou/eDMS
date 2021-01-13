"""
用於加入 自身欄位
"""
from typing import Tuple

from django.urls import reverse

def merge_tuple_element(origin_tuple: Tuple, append_tuple: Tuple
    ) -> Tuple:
    """
    :param origin_tuple: 本身原始有的欄位
    :param append_tuple: 新增的欄位
    :return Tuple: 合併後的欄位
    """
    if origin_tuple is None:
        return append_tuple
    temp_element = list(origin_tuple)
    
    for field in append_tuple:
        if field not in temp_element:
            temp_element.append(field)
    return tuple(temp_element)


def remove_tuple_element(origin_tuple: Tuple, remove_tuple: Tuple
    ) -> Tuple:
    temp_element = list(origin_tuple)
    """
    :param origin_tuple: 
    :param append_tuple:
    :return Tuple: 
    """
    temp_element = list(origin_tuple)
    for field in remove_tuple:
        if field in temp_element:
            temp_element.remove(field)
    return temp_element


def get_html_link(url, display_name):
    html_link = '<a href="{url}">{display_name}</a>'.format(
        url = url,
        display_name = display_name
    )
    return html_link


def get_reverse_link(model_name, reverse_args):
    view_name = model_name
    url_link = reverse(
        view_name,
        args=reverse_args
    )
    return url_link