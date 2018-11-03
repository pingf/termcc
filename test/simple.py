from termcc.cc import cc, dc

from termcc.core import ccc

if __name__ == '__main__':
    print(ccc('yin yang', fore='red'))
    print(ccc('hello', fore='red', back='blue', styles=['bold', 'italic', 'underlined']))
    print(cc(':red: :yin_yang: :green_: hello world :reset:'))
    print(dc('☯  hello world'))
    print(cc('Water! :water_wave:'))
    print(cc('Water! :blue: :water_wave: :yin_yang: :telephone: :yellow_heart: :green_: :red: :world_map: :thumbs_up: :reset:'))
