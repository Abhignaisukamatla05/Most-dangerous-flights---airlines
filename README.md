Its a python code created by Abhigna Isukamatla to do an in-depth analysis of flight data, including arrival times, takeoff times, and delays due to various reasons, over a month in the US.
Contains graphs, visualizations, and statistical measures for comprehensive analysis along with my team.

Airlines can have varying degrees of volatility when it comes to getting people from
point A to point B. Airlines often run into issues such as weather, security threats, late
passengers, etc. and these issues can lead to delayed flights. While all airlines experience issues
and conversely delays, is there an airline someone flies that has a direct affect on the chance that
their flight is canceled or significantly delayed? Based on determining factors such as weather,
late aircrafts, and security delays, there is no clear correlation between the airline someone flies
and the chance that their flight is canceled or significantly delayed.
A program was made using python in order to dissect the information given on flights
within the United States over a given month. In order to make our code easier to work with,
several Python classes assist with abstracting information. The SetOfAirlines class stores a
dictionary of each airline’s data, making it easier to work with. It also automatically converts
unique airline codes into airline names if present, to make charts more readable. For example, the
unique carrier code for United Airlines is “UA”. Most people would not know what “UA”
means, so the SetOfAirlines class has a static dictionary that it checks to see if there is a name
available for that unique carrier code. The class has methods to calculate the the average value of a
column for all airlines, and is easily expandable to include more methods to calculate values and
retrieve information.
Similarly, the Airline class stores a dataframe of a certain airline. The SetOfAirlines
class is designed to store Airline objects. The Airline class has methods to calculate values for
2
that airline, which the SetOfAirlines class uses to perform its calculations. These can also be
easily expanded in the future.
Finally, the SetOfAirlines has a method called fill_na. This method replaces any
instances of NaN (not a number) with 0. When pandas imports the data, it automatically coerces
blank values into NaN. Blank values in the data usually correspond to 0. For example, for
columns like LateAircraftDelay, for flights where no delay was experienced, the value is left
blank. For our purposes, this means there was no delay, hence, the value 0 for 0 delay.
When looking at the average delay for a flight in minutes without reason it is interesting
to see how airline companies are more well known compared to other smaller airlines. There
does not seem to be a correlation between the size of the airline company and how long an
average delay is.This is seen with numbers like American Airlines having an average delay of 27
minutes at the top, but another big name is Southwest Airlines at the bottom with an average
delay of 13 minutes. Continuing to the lesser known airlines there is Jetstream with an average
delay of 25 minutes, and Republic Airlines tied with Southwest Airlines at 13 minutes. These
numbers clearly show that there is no correlation between how well known an airline company is
and how long their average delay is.
The first kind of delay airlines generally experience is delays due to a late aircraft. This is
when planes pull into a terminal behind schedule for a range of reasons. A late aircraft delay can
be caused by a late departure, weather, traffic, etc., and will also extend the delay due to the
boarding process. Airlines must get the previous passengers off the aircraft, clean the plane, and
then begin the boarding process for the next flight causing large delays. Because there are so
many factors that go into a late aircraft delay it is the most impactful delay. This is seen in Chart
3
one depicting the different kinds of delays and how long their delays are on average.
Moreover, late aircrafts are a kind of delay that the airline companies have the most control over
with factors like scheduling and staff to make sure the process runs the most smoothly and as
quickly as possible. Even though airlines have an impact, there are so many exterior impacts that
the odds that a flight is delayed due to late aircrafts is not on an airline.
As mentioned before, weather delays have a large impact on whether a flight is
significantly delayed or canceled. Weather that can delay or cancel a flight consist of
thunderstorms, tornados, hail, hurricanes, blizzards, and flooding. Also on the less harsh side,
things like heavy rain, severe warnings, etc. The AWC, the Federal Aviation Administration
(FAA), and the individual airlines collaborate as a three-party arrangement. However, each
airport makes the final decision about cancellations at that particular airport. Because weather is so volatile and dangerous for planes it causes the most amount of cancellations and is the second
biggest cause for major delays.
Another major kind of delay that airlines must deal with is security delays. According to
an article by the Federal Aviation Administration (FAA) “Security delay is caused by evacuation
of a terminal or concourse, re-boarding of aircraft because of security breach, inoperative
screening equipment and/or long lines in excess of 29 minutes at screening areas.” (Types of
Delay) Security delays are not very common and do not relate to the airline but rather the airport.
Security delay time is also dependent on how capable the airport is when resolving the issue,
whether that issue is a threat or something actually happening.
There are other determining factors when discussing an airline being delayed such as
time in a terminal to load luggage, refuel, and going through safety instructions. There are also
instances when a flight will land late because of rough air conditions causing more turbulence
than usual. Many small factors which are hard to measure with accurate detail create small time
loss, but even though these instances alone are small they begin to pile up. This idea of small
time losses becoming an issue is evident when thinking about the butterfly effect, or in other
words the idea that a small action creates bigger issues down the road. In this case something
small like a 5 minute delay at each stop, when the same aircraft is constantly going from stop to
stop, begins to add up and eventually creates hour long delays for future flights on the same
aircraft.
Overall, delays and cancellations are common when flying in the United States due to
factors such as late aircrafts, severe weather, and security issues. These issues usually have major
connections to the airport and how major of a delay or even a cancellation is. There seems to be
more reliance on an airport and the location a flight would be leaving from to determine whether a flight is able to leave on time, as they control exterior factors such as air traffic, scheduling, and
threats. These are things that individual airlines are unable to control and so significant delays
and cancellations can be placed solely on an airline. However there is no clear correlation
between the airline someone flies and the odds that their flight is canceled or significantly
delayed.
