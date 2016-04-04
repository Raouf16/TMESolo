import math
import random
from soccersimulator import settings
from soccersimulator import SoccerAction 
from soccersimulator import Vector2D


# miroir position
def miroir_p(p):      
    return Vector2D( settings.GAME_WIDTH - p.x,p.y)

# miroir vecteur
def miroir_v(v):	
    return Vector2D(-1*v.x , v.y)  
    
def miroir_sa(action):
    return SoccerAction(miroir_v(action.acceleration),miroir_v(action.shoot))
    
def miroir_st(state):
    res = state.copy()
    res.ball.position = miroir_p(state.ball.position)
    res.ball.vitesse = miroir_v(state.ball.vitesse)
    for (id_team, id_player) in state.players :
        (res.player_state(id_team,id_player)).position = miroir_p(state.player_state(id_team,id_player).position)
        (res.player_state(id_team,id_player)).vitesse = miroir_v(state.player_state(id_team,id_player).vitesse)
    return res    


class PlayerStateDecorator : 
	def __init__(self , state , id_team , id_player):
	
		self.state = state
		self.id_team = id_team
		self.id_player = id_player 



	@property
	def position_balle(self):
		return self.state.ball.position

	@property
	def vitesse_balle(self):
		return self.state.ball.vitesse

	@property
	def position_joueur(self):
		return self.state.player_state(self.id_team, self.id_player).position

	@property
    	def position_defense(self):
        	return self.state.player_state(self.id_team, self.id_player == 0).position
    
   	@property
    	def position_milieu(self):
       		return self.state.player_state(self.id_team, self.id_player == 1).position
    
   	@property
   	def position_milieuDefense(self):
        	return self.state.player_state(self.id_team, self.id_player == 2).position

	@property
   	def position_attaquant(self):
       		return self.state.player_state(self.id_team, self.id_player == 3).position




	@property
	def peutPasser(self):
		return (self.position_balle.distance(self.position_joueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS) 

	@property
	def Passe(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(self.position_coequipier.x, self.position_coequipier.y) - self.position_joueur)
	
	
	@property
	def courirVersBalle(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))



	@property
	def shootDefense(self):
	    	if (self.peutShooter):
			return SoccerAction(self.position_balle - self.position_joueur, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - self.position_joueur)
		else: 
			return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))




def fonceurversballe(Mystate):
	if(Mystate.peutShooter):
		return Mystate.Shoot	
 	else:
             	return Mystate.courirVersBalle



