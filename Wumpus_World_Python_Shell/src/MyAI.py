# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent
from enum import Enum
import random


class MyAI ( Agent ):
    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.Direction = Enum('Direction', 'EAST SOUTH WEST NORTH')
        self.probabilityMap = [[0 for x in range(10)] for y in range(10)]
        self.currentX = 0
        self.currentY = 9
        self.isRetreating = False;
        self.minBoundX = 0
        self.maxBoundX = 9
        self.minBoundY = 0
        self.maxBoundY = 9
        self.currentDirection = self.Direction.EAST
        self.probabilityMap[self.currentY][self.currentX] = 0
        self.wentEast = False
        self.hasGold = False
        self.isRetreating = False
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        # self.probabilityMap[self.currentY][self.currentX] = 0

        if bump is True:
            self.bump_undo()
            self.update_border()
        
        # if stench is False and breeze is False:
        #     return self.move(Agent.Action.FORWARD)
        # else:
        # return self.turn_random()
        
        if(self.wentEast is False):
            if glitter is True:
                self.isRetreating = True
                self.hasGold = True
                return self.move(Agent.Action.GRAB)
            elif self.currentY is self.maxBoundY and self.currentX is self.minBoundX and (stench is True or breeze is True):
                return self.move(Agent.Action.CLIMB)
            elif self.isRetreating is False and (stench is True or breeze is True):
                self.isRetreating = True
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is not self.Direction.WEST:
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is self.Direction.WEST and self.currentY is not self.maxBoundY and self.currentX is not self.minBoundX:
                return self.move(Agent.Action.FORWARD)
            elif self.currentDirection is self.Direction.WEST and self.currentY is self.maxBoundY and self.currentX is self.minBoundX and self.hasGold is True:
                return self.move(Agent.Action.CLIMB)
            elif self.currentDirection is self.Direction.WEST and self.currentY is self.maxBoundY and self.currentX is self.minBoundX and self.isRetreating is True and self.hasGold is False:
                self.wentEast = True
                self.isRetreating = False
                return self.move(Agent.Action.TURN_RIGHT)
            elif self.isRetreating is False and bump is True and self.currentDirection is not self.Direction.WEST:
                self.isRetreating = True
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is self.Direction.NORTH:
                return self.move(Agent.Action.TURN_LEFT)
            else:
                return self.move(Agent.Action.FORWARD)
        elif(self.wentEast is True):
            if glitter is True:
                self.isRetreating = True
                self.hasGold = True
                return self.move(Agent.Action.GRAB)
            elif self.currentY is self.maxBoundY and self.currentX is self.minBoundX and (stench is True or breeze is True):
                return self.move(Agent.Action.CLIMB)
            elif self.isRetreating is False and (stench is True or breeze is True):
                self.isRetreating = True
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is not self.Direction.SOUTH:
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is self.Direction.SOUTH and self.currentY is not self.maxBoundY and self.currentX is not self.minBoundX:
                return self.move(Agent.Action.FORWARD)
            elif self.currentDirection is self.Direction.SOUTH and self.currentY is self.maxBoundY and self.currentX is self.minBoundX and self.isRetreating is True:
                return self.move(Agent.Action.CLIMB)
            elif self.isRetreating is False and bump is True and self.currentDirection is not self.Direction.SOUTH:
                self.isRetreating = True
                return self.move(Agent.Action.TURN_LEFT)
            elif self.isRetreating is True and self.currentDirection is self.Direction.WEST:
                return self.move(Agent.Action.TURN_LEFT)
            else:
                return self.move(Agent.Action.FORWARD)

        # if isRetreating is True:
             # TODO: has gold action


        return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def turn_around(self):
        return Agent.Action.TURN_LEFT

    def turn_random(self):
        turns = [Agent.Action.FORWARD, Agent.Action.TURN_RIGHT, Agent.Action.TURN_LEFT]
        return turns[random.randrange(len(turns))]
        
    def move(self, action):
        if action is Agent.Action.FORWARD:
            if self.currentDirection is self.Direction.EAST:
                self.currentX+=1
            elif self.currentDirection is self.Direction.WEST:
                self.currentX-=1
            elif self.currentDirection is self.Direction.NORTH:
                self.currentY+=1
            else:
                self.currentY-=1
        elif action is Agent.Action.TURN_LEFT or action is Agent.Action.TURN_RIGHT:
            if self.currentDirection is self.Direction.EAST and action is Agent.Action.TURN_LEFT or self.currentDirection is self.Direction.WEST and action is Agent.Action.TURN_RIGHT:
                self.currentDirection = self.Direction.NORTH
            elif self.currentDirection is self.Direction.SOUTH and action is Agent.Action.TURN_LEFT or self.currentDirection is self.Direction.NORTH and action is Agent.Action.TURN_RIGHT:
                self.currentDirection = self.Direction.EAST
            elif self.currentDirection is self.Direction.WEST and action is Agent.Action.TURN_LEFT or self.currentDirection is self.Direction.EAST and action is Agent.Action.TURN_RIGHT:
                self.currentDirection = self.Direction.SOUTH
            else:
                self.currentDirection = self.Direction.WEST

        return action

    def bump_undo(self):
        if self.currentDirection is self.Direction.EAST:
            self.currentX-=1
        elif self.currentDirection is self.Direction.WEST:
            self.currentX+=1
        elif self.currentDirection is self.Direction.NORTH:
            self.currentY-=1
        else:
            self.currentY+=1

    def update_border(self):
        if self.currentDirection is self.Direction.EAST:
            self.maxBoundX = self.currentX
        elif self.currentDirection is self.Direction.NORTH:
            self.minBoundY = self.currentY

    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================