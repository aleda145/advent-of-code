"""
Wasn't solved by myself, I started but took so much time to understand
the description I got help from this: 
https://topaz.github.io/paste/#XQAAAQAPBQAAAAAAAAA0m0pnuFI8c/fBNAn8jP/zLliB/yhToWUPCpV3XwLoiWO/Iydt72UAi6NORl6kmkUlbT/LGStT2k/xurbI9AfeQZFahn1+QSXxWA0MO1ejOTDhxVVdHYLPZ+k4weVvhxtL9ho8hx2+Swc78M1yqPwrbDFeUwTyK1cAgVny/p9R9GStEIQ1lSvWdS1wnK6px2oKVcWYhQNT68aFVg5QkkuVgxOYSuF9hYwofJ64oRefQ9p3Y0pRgxtNsUd7nUAi7s5Z7xtSCQqAi5WvFUd1xiDaq+htmFcr/O+gFoU9Z0+VKHZP6Zp6uxwrm9eEwBY4a1sMQyaf5eH7yIe6Otkbqvya1P/rLWML5vz0VG7pCFFfQ3uwBmH4BwjzYcjmRzpu946xUpHiQZBrkd6riMt12l6Sb+F1FkMBE7T+/gJdzdXtAnyJA30EDtlfTAB3VII6qovoGnBnHfbccGH98Fr2aHvK/fPngL11UvtS4rrHzB1An2VRt2KdscKNq16wfF1NsvjmmKXflcTklcloUjbaZFigHwPmujpxyFLFSpf4Smh0MAwq9TRjtCZ5U8oZbEtzLk7FBuvdw3Lxi8jh64NsJsvFOVXe8BMsDTGq52yiFUd70IJ8mtjsWarz/EU8UC1j3MsNzNIDNP//nidH4A==

"""

import util

inp = util.input_as_string("input")
sample = util.input_as_string("sample_input")

print(inp)
bin_num = ""
for char in inp:
    binny = bin(int(char, 16))[2:]
    bin_num += binny.zfill(4)
print(bin_num)

version_sum = 0


def calc_packet(data):
    global version_sum
    print(f"examine packet: {data}")
    # packet version first 0-3 bits
    package_version = int(data[:3], 2)
    data = data[3:]
    version_sum += package_version
    print(f"version: {package_version}")
    # packet type 3-5 bits
    packet_type = int(data[:3], 2)
    data = data[3:]
    print(f"type: {packet_type}")

    if packet_type == 4:
        print("literal packet!")
        # literal value
        # always four bits + leading bit
        package_values = ""
        while True:
            first_bit = data[0]
            package = data[1:5]
            data = data[5:]
            print(package)
            package_values += package
            # if a packet starts with 0 it means its last
            # discard anything afterwards
            if first_bit == "0":
                print(f"value was: {int(package_values,2)}")
                print(f"data left {data}")
                break
    else:
        print("operator packet")
        # if packet type != 4 then it is an operator
        # The bit after the packet type if !=4
        # is the length type ID
        length_type = data[0]
        data = data[1:]
        if length_type == "0":
            print("length_type 0")
            # look at next 15 bits
            next_bits = data[:15]
            data = data[15:]
            # print(next_bits)
            assert len(next_bits) == 15
            length_sub_packets = int(next_bits, 2)
            # print(length_sub_packets)
            subpackets = data[:length_sub_packets]
            while subpackets:
                subpackets = calc_packet(subpackets)
            data = data[length_sub_packets:]
        elif length_type == "1":
            print("length_type 1")
            next_bits = data[:11]
            data = data[11:]
            print(next_bits)
            # assert len(next_bits) == 11
            number_sub_packets = int(next_bits, 2)
            for i in range(number_sub_packets):
                data = calc_packet(data)
    return data


calc_packet(bin_num)
print(f"versio sum: {version_sum}")
