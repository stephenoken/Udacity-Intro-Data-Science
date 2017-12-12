from functools import reduce


def write_key_value_pairs(output_filename, output_dict, *keys):
    str_body = reduce(lambda cur_str, key: cur_str + "{}\t".format(output_dict[key]), keys[:-1], "")
    output_str = str_body + "{}\n".format(output_dict[keys[-1]])
    with open(output_filename, "a") as output_file:
        output_file.write(output_str)


def contains(keys, key):
    return keys.count(key) > 0


def count_entries(key_values_dict, key_value):
    key, value = key_value.strip().split("\t")
    keys = list(key_values_dict)
    count = key_values_dict[key] + float(value) if contains(keys, key) else float(value)
    key_values_dict[key] = count
    return key_values_dict


def write_to_file(output_filename, content):
    with open(output_filename, "a") as text_file:
        text_file.write(content)
