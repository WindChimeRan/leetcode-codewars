-- https://www.codewars.com/kata/transform-an-array-into-a-string/train/haskell
module Transform.Kata (transform) where

transform :: Show a => [a] -> String
transform = concat . map show
