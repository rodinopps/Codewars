def get_size(w,h,d):
    area = (w * h + w * d + h * d) * 2
    volume = w * h * d
    return [area, volume]
