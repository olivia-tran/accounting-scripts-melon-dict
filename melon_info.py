"""Print out all the melons in our inventory."""
from melons import melon_data


# def track_melon_info(melon_data):
#     """accept melon data and print each melon with corresponding attributes"""
#     for melon_type in melon_data:  # loop over melon_data's keys aka different melon types
#         print(f'\n{melon_type.upper()}')
#         # loop over the values of melon types and unpack both keys and values
#         for k, v in melon_data[melon_type].items():
#             print(f'{k}: {v}')
#         print('\n=================================')


# track_melon_info(melon_data)

"""Below is a 2nd way to do it, looping over k, v twice"""


def print_melon_info(melon_data):
    """accept melon data and print each melon with corresponding attributes"""
    for melon_name, attributes in melon_data.items():
        print(f'\nmelon_name.upper()')
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
        print(f'\n==============================')


print_melon_info(melon_data)
