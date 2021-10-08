import turtle
import pandas

score = 0

# CONGIGURE MAP
screen = turtle.Screen()
screen.setup(1200, 1000, startx=360, starty=0)
screen.screensize(1190, 990)
screen.title("GeoGame")
image = "france_map.gif"
screen.addshape(image)
turtle.shape(image)

# HELP TURTLE
t_help = turtle.Turtle()
t_help.hideturtle()
t_help.penup()
t_help.speed(0)
t_help.goto(-500, 470)
t_help.color("green")
t_help.write("AIDE : RESPECTEZ LE FORMAT SUIVANT : Alpes-de-Haute-Provence",
             align='left',
             font=('Arial', 14, 'normal'))

# EXIT TURTLE
t_exit = turtle.Turtle()
t_exit.hideturtle()
t_exit.penup()
t_exit.speed(0)
t_exit.goto(0, -490)
t_exit.color("RED")
t_exit.write("'q' pour quitter",
             align='center',
             font=('Arial', 14, 'normal'))

# DPT TEXT TURTLE
t_dpt_text = turtle.Turtle()
t_dpt_text.hideturtle()
t_dpt_text.penup()
t_dpt_text.speed(0)

# SCORE TURTLE
t_score = turtle.Turtle()
t_score.hideturtle()
t_score.penup()
t_score.speed(0)
t_score.goto(500, 470)
t_score.color("blue")
t_score.write(f"SCORE : {score} / 101",
              align='right',
              font=('Arial', 14, 'normal'))

success_list = []
missed_list = []

# ---------- FUNCTION TO GET COORD ON CLICK -------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
# -------------------------------------------------------------


# GET CSV DATA
data = pandas.read_csv("departements.csv")
dpt_data_list = data.departement.to_list()

while len(success_list) < 101:
    answer_dpt = screen.textinput(title="Connais-tu les 101 départements ?", prompt="Entrer un département")

    if answer_dpt == 'q':
        break
    if answer_dpt in dpt_data_list:
        dpt = data[data.departement == answer_dpt]
        coord = (int(dpt.x), int(dpt.y))
        t_dpt_text.goto(coord)
        t_dpt_text.write(answer_dpt, align='left', font=('Arial', 10, 'normal'))
        success_list.append(answer_dpt)
        score += 1
        t_score.clear()
        t_score.write(f"SCORE : {score} / 101", align='right', font=('Arial', 14, 'normal'))

if len(success_list) == 101:
    t_help.clear()
    t_help.goto(-500, 470)
    t_help.write("Félicitations ! Vous connnaissez tous les départements français.",
                 align='center',
                 font=('Arial', 14, 'normal'))

else:
    for item in dpt_data_list:
        if item not in success_list:

            missed_list.append(item)

    for item in missed_list:
        dpt = data[data.departement == item]
        coord = (int(dpt.x), int(dpt.y))
        t_dpt_text.color("red")
        t_dpt_text.goto(coord)
        t_dpt_text.write(item, align='left', font=('Arial', 10, 'normal'))


    # df = pandas.DataFrame(missed_list)

screen.exitonclick()
