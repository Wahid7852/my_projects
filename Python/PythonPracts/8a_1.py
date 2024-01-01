import geometry_8a as geometry

def pointyShapeVolume(x, y, squareBase):
    if squareBase:
        base_area = geometry.squareArea(x)
        return (1/3) * base_area * y
    else:
        base_area = geometry.circleArea(x)
        return (1/3) * base_area * y

x = float(input("Enter the length of an edge of the square or the radius of the circle: "))
y = float(input("Enter the height of the object: "))
squareBase = input("Is the base square (True/False)? ").strip().lower() == "true"

if squareBase:
    shape_type = "square pyramid"
else:
    shape_type = "right circular cone"

volume = pointyShapeVolume(x, y, squareBase)
print(f"Volume of the {shape_type}: {volume:.2f}")
