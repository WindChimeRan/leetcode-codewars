-- 1
module Cycle where

import Data.List (elemIndex)

data Direction = L | R deriving (Show)

cycleList :: (Eq a) => Direction -> [a] -> a -> Maybe a
cycleList L xs x = 
        case x `elemIndex` xs of
            Just n  -> Just ((xs ++ xs) !! (n - 1 + (length xs)))
            Nothing -> Nothing
cycleList R xs x = 
        case x `elemIndex` xs of
            Just n  -> Just ((xs ++ xs) !! (n + 1))
            Nothing -> Nothing
-- 2
module Cycle where

import Data.List (elemIndex)

data Direction = L | R deriving (Show)

cycleList :: (Eq a) => Direction -> [a] -> a -> Maybe a
cycleList d xs x = 
            do
              i <- elemIndex x xs
              pure $ (xs ++ xs) !! (index d i xs)
              where index L i xs = i - 1 + (length xs)
                    index R i xs = i + 1
-- 3
module Cycle where

import Data.List (elemIndex)

data Direction = L | R deriving (Show)

cycleList :: (Eq a) => Direction -> [a] -> a -> Maybe a
cycleList d xs x = do 
  i <- elemIndex x xs 
  return $ xs !! (dir i `mod` length xs)
  where dir = case d of L -> pred
                        R -> succ
