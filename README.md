# Predictive Maintenance
## Notes for the data: 
PGNs pertaining to engines, brakes, fan status, braking controls, and fluids selected to focus on most common faults. Another consideration could be the PGN labeled "Hybrid System" and "Vehicle Electrical Power 1". \
Only sensor readings are chosen and status requests and feedbacks are not chosen.\
Some Engine Aftertreatment System Details are ommitted to avoid complexity in introducing and detecting potential faults. These features are not considered very relevant due to the low number of records. \
Engine Hours information and Vehicle Distance (Total) could be ommitted as it may be lower for newer buses but these values are no cause for concern. \
Engine Instantaneous Fuel Economy maybe very rough due to varying speeds constantly, however, Engine Average Fuel Economy could be more insightful and easier to deal with. \
For the Engine Cooling System, Engine Fuel Temperature and Engine Oil Temperature Sensors do not give any valuable/sensible readings so only the coolant related
parameters are used, mainly coolant temperature and coolant level. \

## Additional Notes
Learn more about the DCGAN architecture used in Gretel's model (such as the distribution they sample from, etc). \
Mention about the Hybrid system of the bus used for data collection and justify the choice of sensor readings selected (a more universal appraoch to incoporate combustion engines due to the common features and so on).\
Data processing generates a large csv file with each spn as a column.
Every time series entry is a row for a particular PGN-SPN pair,
the remaining columns are filled with NULL which are then replaced by
forward fill values as the sensor values are either updated at regular intervals or at changes.
The data generation file has been modified to read the new csv and
include the relevant columns as attributes.


