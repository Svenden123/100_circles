import simple_draw as sd


def bubble(point, step):
    radius = 50
    for _ in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5)

sd.pause()