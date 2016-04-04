import math
import random
from soccersimulator import settings
from soccersimulator import SoccerAction 
from soccersimulator import Vector2D





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
    	def position_joueur1(self):
        	return self.state.player_state(self.id_team, self.id_player == 0).position

	@property
    	def position_joueur2(self):
        	return self.state.player_state(self.id_team, self.id_player == 1).position

	@property
    	def position_joueur3(self):
        	return self.state.player_state(self.id_team, self.id_player == 2).position

	@property
    	def position_joueur4(self):
        	return self.state.player_state(self.id_team, self.id_player == 3).position



	@property
	def peutShooterVitesse(self):
		return self.state.player_state(self.id_team, self.id_player).vitesse < 0.01

	@property
	def peutPasser(self):
		return (self.position_balle.distance(self.position_joueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS) 




	@property
	def Passe1(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(self.position_joueur1.x, self.position_joueur1.y) - self.position_joueur)
	@property
	def Passe2(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(self.position_joueur2.x, self.position_joueur2.y) - self.position_joueur)
	@property
	def Passe3(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(self.position_joueur3.x, self.position_joueur3.y) - self.position_joueur)
	@property
	def Passe4(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(self.position_joueur4.x, self.position_joueur4.y) - self.position_joueur)

	

	@property
	def replacementPasseur1(self):
		return SoccerAction(Vector2D(settings.GAME_WIDTH/2+10, settings.GAME_HEIGHT/2 - 10) - self.position_joueur, Vector2D(0,0))

	@property
	def replacementPasseur2(self):
		return SoccerAction(Vector2D(settings.GAME_WIDTH/2-10, settings.GAME_HEIGHT/2 - 10) - self.position_joueur, Vector2D(0,0))

	@property
	def replacementPasseur3(self):
		return SoccerAction(Vector2D(settings.GAME_WIDTH/2+10, settings.GAME_HEIGHT/2 + 10) - self.position_joueur, Vector2D(0,0))

	@property
	def replacementPasseur4(self):
		return SoccerAction(Vector2D(settings.GAME_WIDTH/2+10, settings.GAME_HEIGHT/2 + 10) - self.position_joueur, Vector2D(0,0))



	
	@property
	def courirVersBalle(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))

	@property
	def Shoot(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - self.position_joueur)






def fonceurversballe(Mystate):
	if(Mystate.peutShooter):
		return Mystate.Shoot	
 	else:
             	return Mystate.courirVersBalle



def passeur1(Mystate):
	if(self.id_player == 3)
		if(Mystate.peutShooter):
			if(Mystate.peutShooterVitesse):
				return Mystate.Passe1
		else:
			return Mystate.replacementPasseur1

def passeur2(Mystate):
	if(self.id_player == 0)
		if(Mystate.peutShooter):
			if(Mystate.peutShooterVitesse):
				return Mystate.Passe2
		else:
			return Mystate.replacementPasseur2

def passeur3(Mystate):
	if(self.id_player == 1)
		if(Mystate.peutShooter):
			if(Mystate.peutShooterVitesse):
				return Mystate.Passe3
		else:
			return Mystate.replacementPasseur3

def passeur4(Mystate):
	if(self.id_player == 2)
		if(Mystate.peutShooter):
			if(Mystate.peutShooterVitesse):
				return Mystate.Passe4
		else:
			return Mystate.replacementPasseur4




