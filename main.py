import random
import math
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

maxspeed = 0.04
speed = 0.008
friction = 0.004
rotation = 0
app = Ursina()

window.size = (1920, 1080)
balls = []

shoot_pressed = False

xvelo = 0
zvelo = 0

redscoreflipped = False

bluescoreflipped = True


blueballs = 0
redballs = 0
# Flat ground


ground = Entity(
    model='plane',
    scale=(12, 1, 12),
    texture='white_cube',
    texture_scale=(6, 6),
    collider='box',
    position=(0, 0, 0),
)

arm1 = Entity(
    model='armoneside.obj',
    scale=(3.3, 3.3, 3.3),
    texture='blue.png',
    texture_scale=(1, 1),
    collider='box',
    position=(0, 0, 0),
    rotation=(-90, 0, 0)
)


arm = Entity(
    model='armoneside.obj',
    scale=(3.3, 3.3, 3.3),
    texture='red.jpg',
    texture_scale=(1, 1),
    collider='box',
    position=(0, 0, 0),
    rotation=(-90, 180, 0)
)

topbar = Entity(
    model='topbar.obj',
    scale=(3.3, 3.5, 3.3),
    texture='blue.png',
    texture_scale=(1, 1),
    collider='box',
    position=(-1.05, 3.4, 0),
    rotation=(-90, 90, 0)
)



#scor areas
scoringareabackrightdown = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='red.jpg',
    texture_scale=(1, 1),
    collider='box',
    position=(1, 3, -1.5),
    rotation=(-110, 0, 3)
)
#scoringareabackrightdown.visible = False

scoringareabackrightup = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='green.png',
    texture_scale=(1, 1),
    collider='box',
    position=(1, 4, -1.5),
    rotation=(-70, 0, 3)
)
#scoringareabackrightdown.visible = False



scoringareabackleftdown = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='red.jpg',
    texture_scale=(1, 1),
    collider='box',
    position=(-1, 3, -1.5),
    rotation=(-110, 0, 3)
)
#scoringareabackrightdown.visible = False

scoringareabackleftup = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='green.png',
    texture_scale=(1, 1),
    collider='box',
    position=(-1, 4, -1.5),
    rotation=(-70, 0, 3)
)
#scoringareabackrightdown.visible = False



scoringareafrontleftdown = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='red.jpg',
    texture_scale=(1, 1),
    collider='box',
    position=(-1, 3, 1.5),
    rotation=(-70, 0, 3)
)
#scoringareafrontrightdown.visible = False

scoringareafrontleftup = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='green.png',
    texture_scale=(1, 1),
    collider='box',
    position=(-1, 4, 1.5),
    rotation=(-110, 0, 3)
)
#scoringareabackrightdown.visible = False






scoringareafrontrightdown = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='red.jpg',
    texture_scale=(1, 1),
    collider='box',
    position=(1, 3, 1.5),
    rotation=(-70, 0, 3)
)
#scoringareafrontrightdown.visible = False

scoringareafrontrightup = Entity(
    model='cube',
    scale=(1.1, 1, 0.7),
    texture='green.png',
    texture_scale=(1, 1),
    collider='box',
    position=(1, 4, 1.5),
    rotation=(-110, 0, 3)
)
#scoringareabackrightdown.visible = False






arrow = Entity(
    model='arrow',
    scale=(0.5, 0, 1),
    texture='white_cube',
    texture_scale=(1, 1),
    collider='box',
    position=(0, 0.51, 0),
)



leftwall = Entity(
    model='plane',
    scale=(1, 1, 12),
    texture='brick',
    texture_scale=(2, 24),
    collider='box',
    position=(-6, 0.5, 0),
    rotation=(0, 0, 90), 
)



rightwall = Entity(
    model='plane',
    scale=(1, 1, 12),
    texture='brick',
    texture_scale=(2, 24),
    collider='box',
    position=(6, 0.5, ),
    rotation=(0, 0, 270), 
)


backwall = Entity(
    model='plane',
    scale=(1, 1, 12),
    texture='brick',
    texture_scale=(2, 24),
    collider='box',
    position=(0, 0.5, 6),
    rotation=(0, 90, 90), 
)
backwall = Entity(
    model='plane',
    scale=(1, 1, 12),
    texture='brick',
    texture_scale=(2, 24),
    collider='box',
    position=(0, 0.5, -6),
    rotation=(0, 90, 90), 
)









Sky()

# A few colored blocks so you can tell you're moving



camera.position = (3, 11, -11)      # where the camera sits (x, height, z)
camera.look_at(Vec3(0, 0, 0))       # point it at the middle of the field
camera.fov = 70                     # optional: wider view


cube = Entity(
    model='cube',
    color=color.azure,
    position=(0.5, 0.25, 0.5),
    scale=(1, 0.5, 1),
    rotation=(0, 0, 0),      # turn it 45° around the vertical axis
    texture='white_cube',     # adds a grid pattern
    collider='box',           # makes it solid (needed for walking into it or clicking it)
)

def update():
    cube.rotation_y = 0
    
    global xvelo, zvelo, rotation, shoot_pressed, balls, arrow, arm1, scoringareabackrightdown, scoringareabackrightup, scoringareabackleftdown, scoringareabackleftup, scoringareafrontleftdown, scoringareafrontleftup, scoringareafrontrightdown, scoringareafrontrightup, redscoreflipped, bluescoreflipped
    if redscoreflipped:
        scoringareabackrightdown.enabled = False
        scoringareabackrightup.enabled = True
        
        scoringareafrontrightdown.enabled = True;
        scoringareafrontrightup.enabled = False
    else:

        scoringareabackrightdown.enabled = True
        scoringareabackrightup.enabled = False
        
        scoringareafrontrightdown.enabled = False
        scoringareafrontrightup.enabled = True
    


    if bluescoreflipped:
        scoringareabackleftdown.enabled = False
        scoringareabackleftup.enabled = True
        
        scoringareafrontleftdown.enabled = True;
        scoringareafrontleftup.enabled = False
    else:

        scoringareabackleftdown.enabled = True
        scoringareabackleftup.enabled = False
        
        scoringareafrontleftdown.enabled = False
        scoringareafrontleftup.enabled = True
        
        
        
        
    if mouse.right:
        camera.rotation_y += mouse.velocity[0] * 40
        camera.rotation_x = clamp(camera.rotation_x - mouse.velocity[1] * 40, -90, 90)
        camera.position += (camera.forward * (held_keys['w'] - held_keys['s']) + camera.right * (held_keys['d'] - held_keys['a']) + Vec3(0, 1, 0) * (held_keys['e'] - held_keys['q'])) * time.dt * 10
    
    if held_keys['w'] and not mouse.right:
        
        zvelo += speed
    if held_keys['s'] and not mouse.right:
       
        zvelo -= speed
    if held_keys['a'] and not mouse.right:
        
        xvelo -= speed
    if held_keys['d'] and not mouse.right:
        xvelo += speed
    
    
    
    if held_keys['left arrow']:
        
        rotation -= 2
    if held_keys['right arrow']:
        rotation += 2


    
    
    
    if xvelo > 0:
        xvelo -= friction
    if xvelo < 0:
        xvelo += friction
    
    if zvelo > 0:
        zvelo -= friction
    if zvelo < 0:
        zvelo += friction
        
        
    if zvelo < -maxspeed:
        zvelo = -maxspeed
        
    if zvelo > +maxspeed:
        zvelo = +maxspeed
        
        
    if xvelo < -maxspeed:
        xvelo = -maxspeed
    if xvelo > +maxspeed:
        xvelo = +maxspeed 

    
    
    cube.x += xvelo
    if cube.intersects(ignore=[ground, arm1] + balls).hit:
        cube.x -= xvelo
        xvelo = 0
    
    
    
    
    
    
    cube.z += zvelo
    if cube.intersects(ignore=[ground, arm1] + balls).hit:
            cube.z -= zvelo
            zvelo = 0
        
        
        
           
        
        
        
    cube.rotation_y = rotation
    arrow.rotation_y = rotation
    arrow.x = cube.x
    arrow.z = cube.z
    if shoot_pressed == True:
        
        shoot_pressed = False
        balls.append(Entity(model='sphere',scale=(0.2, 0.2, 0.2),texture='grass',texture_scale=(1, 1),collider='box',position=(cube.x, 1, cube.z),rotation=(0, 90, 90),yvelocity=0.112, xvelocity=xvelo + math.cos(math.radians(rotation)) * 0.02, zvelocity=zvelo + math.cos(math.radians(rotation + 90)) * 0.02))
        
    
    if (len(balls) > 0):
        for ball in balls:
            ball.y += ball.yvelocity
            ball.x += ball.xvelocity
            ball.z += ball.zvelocity
            ball.yvelocity = ball.yvelocity - 0.002
            print(ball.yvelocity)
            
            
    

    



def input(key):
    global shoot_pressed, camera
    if key == 'escape':
        application.quit()
    if key == 'f':
        print("SHOOTING")
        shoot_pressed = True
    
        


app.run()