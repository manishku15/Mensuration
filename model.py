import streamlit as st
import math



st.set_page_config(
    page_title="Mensuration",
    page_icon=":rocket:",
    layout="wide"  # Set layout (wide or centered)

)


# Load custom CSS from file
with open("custom.css", "r") as f:
    custom_css = f.read()
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)



st.write('<span style="font-size: 24px; color: green;">You are welcome!</span>', unsafe_allow_html=True)

st.markdown("# Mensuration understanding and formula")
st.markdown("manishpcm6@gmail.com")

st.title('Mensuration')
html_temp= """
    <div style="background-color:rgb(139, 7, 0) ;padding:15px">
    </div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

custom_css = """
<style>
body {
    background-color: #F5F5F5;
    font-family: Arial, sans-serif;
}

h1 {
    color: #009688;
    font-size: 2.5rem;
}

h2 {
    color: #00796B;
    font-size: 2rem;
}

.button-primary {
    background-color: #009688;
    color: #FFFFFF;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.button-secondary {
    background-color: #FF5722;
    color: #FFFFFF;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.button-primary:hover {
    background-color: #00766C;
}

.button-secondary:hover {
    background-color: #E64A19;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)



dece='''What is Mensuration?

Mensuration is a branch of mathematics that deals with the measurement of 
geometric figures and their properties, including length, area, volume, 
and other related quantities. It is concerned with the study of various shapes 
and their dimensions in two-dimensional (2D) and three-dimensional (3D) space.
Mensuration plays a crucial role in geometry and is used in various real-world applications,
such as calculating the area of land, volume of containers, and more.

The concept of area in mensuration refers to the measure of the amount of 
space enclosed by a two-dimensional shape or surface.There are various formulas
 to calculate the area of different types of 2D shapes,some of which include:

Rectangle: The area of a rectangle is given by the formula A = length × width
 where "A" represents the area, and "length" and "width" are the dimensions of the rectangle.

Sphere:
A sphere is like a perfectly round ball. It's a 3D shape where all points on its surface are the same distance from its center.
 The key formulae for a sphere are:

Radius (r): The distance from the center of the sphere to its surface.
Circumference: The distance around the sphere: Circumference = 2 * π * Radius.
Surface Area: The total area of the sphere's surface: Surface Area = 4 * π * Radius².
Volume: The space enclosed by the sphere: Volume = (4/3) * π * Radius³.

Cone:
A cone is like a party hat. It's a 3D shape with a circular base that narrows to a single point at the top. 
The main formulae for a cone are:

Radius (r): The distance from the center of the circular base to its edge.
Height (h): The distance from the base to the top point.
Slant Height (l): The distance from the base's edge to the top point.
Surface Area: The total area of the cone's surface: Surface Area = π * Radius * (Radius + l).
Volume: The space enclosed by the cone: Volume = (1/3) * π * Radius² * Height.

Cube:
A cube is like a box with six equal square sides. It's a 3D shape with all edges and angles equal. 
The main formulae for a cube are:

Edge Length (a): The length of one side of the cube.
Surface Area: The total area of the cube's six square faces: Surface Area = 6 * a².
Volume: The space enclosed by the cube: Volume = a³.

What is Volume?
Volume, in the context of mensuration, refers to the measure of 
the amount of space enclosed by a three-dimensional (3D) object or solid shape. 
It is the quantity that represents how much space is occupied by the object.
The formula for calculating the volume of different 3D shapes varies depending on the shape.

Here are a few examples:
Cube: The volume of a cube is given by V = side × side × side
 where "V" is the volume, and "side" is the length of one side of the cube.
Sphere: The volume of a sphere is calculated as V = (4/3)πr^3 
where "V" is the volume, "r" is the radius of the sphere, and π (pi) is approximately 3.14159.
Cylinder: The volume of a cylinder is given by V = πr^2h
 where "V" is the volume, "r" is the radius of the base, and "h" is the height of the cylinder.
Cuboid or Rectangular Prism: The volume of a cuboid is calculated as V = length × width × height
 where "V" is the volume, and "length," "width," and "height" are the dimensions of the cuboid.
Like with area, there are specific formulas for finding the volume of various 3D shapes and solids,
and these formulas are essential for solving problems involving the measurement of space in three dimensions.'''




class Sphere:
    def __init__(self,radius):
        self._radius=radius
    def full_sphere(self):
        area=4*math.pi*self._radius**2
        return area
    def half_sphere(self):
        Area= 2*math.pi*self._radius**2
        return Area
    def volume_full_sphere(self):
        volum= (4/3)*math.pi*self._radius**3
        return volum
    def volume_half_sphere(self):
        volume2=(2/3)*math.pi*self._radius**3
        return volume2
    
class cone:
    def __init__(self,radius , height):
        self._radius=radius
        self._height=height
    def cone_curved_area(self):
        length=math.sqrt(self._radius**2+self._height**2)
        curved_area=math.pi*self._radius*length
        return curved_area
    def cone_surface_area(self):
        length=math.sqrt(self._radius**2+self._height**2)
        surface_area=math.pi*self._radius*(length+self._radius)
        return surface_area
    def cone_volume(self):
        volume=1/3*math.pi*self._radius**2*self._height
        return volume
    def cone_circumference(self):
        circumference=2*math.pi*self._radius
        return circumference
    
class Cube:
    def __init__(self, side):
        self._side=side
    def cube_area(self):
        area=6*self._side**2
        return area
    def cube_length_diagonal_face(self):
        length1=math.sqrt(2*self._side)
        return length1
    def cube_Diagonal_length(self):
        legth2=math.sqrt(3*self._side)
        return legth2
    def volume(self):
        vol=(self._side**3)
        return vol
    

        
    
Function=st.sidebar.radio('Select Shape',('Understanding of Formula','Sphare',"Cone", "Cube"))
if Function=='Understanding of Formula':
    st.header("Understanding of Formula")
    st.write(dece)
elif Function=='Sphare':
    st.header("Sphere")
    radiuss = st.number_input('Radius')
    st.write('The current radius is ', radiuss)
    sp=Sphere(radiuss)
    area=sp.full_sphere()
    volume=sp.volume_full_sphere()
    Half_area=sp.half_sphere()
    half_volume=sp.volume_half_sphere()
    selected_formula = st.selectbox("Select Formula", ["Area", "Volume","Half_area","half_volume"])
    if selected_formula=="Area":
        st.write('A=4πr2')
        st.write("Area",round(area,2))
    elif selected_formula=="Volume":
        st.write('V=4/3πr**3')
        st.write("Full Volume",round(volume,2))
    elif selected_formula=="Half_area":
        st.write('A=4/3(πr2)')
        st.write("Full Volume",round(Half_area,2))
    else:
        st.write('Volume=(3/2)πr**3')
        st.write("Full Volume",round(half_volume,2))
if Function=='Cone':
    st.header("Cone")
    radiuss1 = st.number_input('Radius')
    st.write('The current radius is ', radiuss1)
    heights = st.number_input('Height')
    st.write('The current radius is ', heights)
    con=cone(radiuss1,heights)
    cone_surface_area=con.cone_surface_area()
    cone_curved_area=con.cone_curved_area()
    cone_volume=con.cone_volume()
    cone_circumference=con.cone_circumference()
    selected_formula = st.selectbox("Select Formula", ["Area", "Volume","Half_area","cone_circumference"])
    if selected_formula=="Area":
        st.write("Area",round(cone_surface_area,2))
    elif selected_formula=="cone_curved_area":
        st.write("Curved Area",round(cone_curved_area,2))
    elif selected_formula=="Volume":
        st.write('V=(πr**2)h/3')
        st.write("Volume",round(cone_volume,2))
    else:
        st.write("Circumference",round(cone_circumference,2))


if Function=='Cube':
    st.header("Cube")
    Side = st.number_input('Side')
    st.write('Side of Cube', Side)
    cub=Cube(Side)
    c_area=cub.cube_area()
    c_d_length=cub.cube_Diagonal_length()
    c_l_d_f=cub.cube_length_diagonal_face()
    c_vol=cub.volume()
    selected_formula = st.selectbox("Select Formula", ["Area", "Volume","Dialonal length","Cube side face length"])
    if selected_formula=="Area":
        st.write("Area",round(c_area,2))
    elif selected_formula=="Dialonal length":
        st.write("Dialonal length",round(c_d_length,2))
    elif selected_formula=="Volume":
        st.write("Volume",round(c_vol,2))
    else:
        st.write("Cube side face length",round(c_l_d_f,2))











