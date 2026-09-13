# What I checked, and what the agent got wrong

Write this yourself, in your own words. It is the part of the repo that proves the work is yours.

## What the agent got wrong
The agent tried to push to GitHub on its own and failed it didn't have
access to my sulemanxcoder account and kept getting a 403 error. It also
assumed it could just run the push without asking me for credentials first.
I had to navigate to the right folder myself and run the push command manually.

## What I checked before I accepted its work
I ran pytest myself after the fixes and confirmed all 4 tests pass, including
the new one I asked the agent to add. I also checked that SERVICE_INTERVAL_KM
is still 15000 and WARN_AT_PERCENT is still 80 in the code neither was
touched. I read the wear_percent function to confirm it now uses / not //,
which is why 14900 km now correctly shows as ~99% worn instead of 0%.

## What the data actually said
The strongest predictor of a breakdown was km_since_service cars that broke
down had gone more than twice as far without a service compared to healthy cars
(13,000 km vs 6,300 km median). Daily usage and load factor also mattered.
The surprising finding was that total odometer reading and age had almost zero
difference between the two groups the obvious guesses turned out to be wrong.
