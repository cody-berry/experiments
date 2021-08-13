# I learned about particle textures in Coding Train's Nature of Code 2
# video, 4.4: Particle Systems with Image Textures:
# Link: https://www.youtube.com/watch?v=pUhv2CA0omA
# With Daniel
# Texturegen stands for Texture Generator which generates a texture. 
# We're going to plug this into Particle to make a fuzzy object. 
# Cody
# 2021, August 8/12, 12:50 PM


def setup():
    global pg
    size(32, 32)
    
    # If we don't use createGraphics() to do this, because save doesn't save transparency,
    # we need to use createGraphics. createGraphics is completely transparent, and saving
    # it will get you an image with transparency. 
    pg = createGraphics(width, height)
    
            
def draw():
    global pg
    background(0)
    
    r = width/2 # The radius of the texture
    cx = width/2 # The x-coordinate of the center of the particle texture
    cy = height/2 # The y-coordinate of the center of the particle texture
    
    pg.beginDraw()    
    for i in range(width):
        for j in range(height):
            # We wanna map so that pixels far away from the screen are dark while ones
            # closer to the middle are lighter. 
            b = map(dist(i, j, cx, cy), r, 0, 0, 255)
            # If we do just stroke(), pg won't use it, so we need to use pg.stroke()
            # so that we can effect pg.point().
            pg.stroke(255, 255, 255, b)
            # We need to show the particle texture, but we need to show it in its
            # appropriate position, the coordinate x, y. If we don't pg.point(), we
            # won't see anything.
            pg.point(i, j)
    pg.endDraw()
    
    
    # To show our texture, we need to draw an image of pg.
    image(pg, 0, 0)
    noLoop()
    pg.save("texture.png")
