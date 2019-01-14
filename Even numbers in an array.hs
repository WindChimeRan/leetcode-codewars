-- https://www.codewars.com/kata/even-numbers-in-an-array/train/haskell
module EvenNums where 

evenNumbers :: [Int] -> Int -> [Int]
evenNumbers xs n = reverse. take n . reverse . filter even $ xs
