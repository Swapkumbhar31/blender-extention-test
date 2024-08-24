import bpy


def register():
   print("Hello from custom extension")


def unregister():
   print("Goodbye from custom extension")


if __name__ == "__main__":
    register()