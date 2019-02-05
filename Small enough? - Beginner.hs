-- https://www.codewars.com/kata/small-enough-beginner/train/haskell
-- 1
module Kata where

smallEnough :: [Int] -> Int -> Bool
smallEnough xs v = all (<= v) xs
