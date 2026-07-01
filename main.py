# IB Physics Kinematics Calculator (d = vt + 0.5at^2)
print("--- STEM Kinematics Analysis Tool ---")

vi = float(input("Enter initial velocity (m/s): "))
a = float(input("Enter acceleration (m/s^2): "))
t = float(input("Enter time elapsed (seconds): "))

# Kinematic displacement formula
displacement = (vi * t) + (0.5 * a * (t ** 2))

print(f"\nThe total displacement of the object is: {displacement} meters.")