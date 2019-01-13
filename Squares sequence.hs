-- https://www.codewars.com/kata/squares-sequence/train/haskell

-- 1
module Codewars.Exercise.Squares where

squares :: Integer -> Int -> [Integer]
squares x n = [x^2^(t-1) | t <- [1..n]]

-- 2
module Codewars.Exercise.Squares where

squares :: Integer -> Int -> [Integer]
squares x n = take n . iterate (^2) $ x
