-- 1
module Banjo where

areYouPlayingBanjo :: String -> String
areYouPlayingBanjo all@('r':rs) = all ++ " plays banjo" 
areYouPlayingBanjo all@('R':rs) = all ++ " plays banjo" 
areYouPlayingBanjo rs = rs ++ " does not play banjo"

-- 2
module Banjo where

areYouPlayingBanjo :: String -> String
areYouPlayingBanjo name@(c:_) 
  | c `elem` "rR" = name ++ " plays banjo"
  | otherwise = name ++ " does not play banjo"
