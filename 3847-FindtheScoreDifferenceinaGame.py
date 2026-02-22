"""
Problem: 3847. Find the Score Difference in a Game
Link: https://leetcode.com/problems/find-the-score-difference-in-a-game/

Level: Easy

Description:
You are given an integer array nums representing the scores gained in each round of a game.

Two players play the game by taking turns picking elements from the array according to the rules defined in the problem.

Your task is to compute the difference between the total scores of the two players after all rounds are completed.

Return the final score difference.

Example:

Input:

nums = [2,5,4,1]

Output:

2
"""
class Solution(object):
    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        player1= True
        player2 = False
        p1 = 0
        p2 =0
        for i in range(len(nums)):
            if (i+1)%6==0:
                player1,player2 = player2,player1
            if nums[i]%2!=0:
                player1,player2 = player2,player1
            if player1 == True:
                p1+=nums[i]
            else:
                p2+=nums[i]
        return p1-p2