# BookingGuard — Problem Card

## Business question
Which bookings are likely to cancel, so the revenue team can overbook safely?

## Prediction target
is_canceled (1 = cancelled, 0 = stayed). Binary classification.

## When is the prediction made?
At booking time. Only use information known at that moment.

## Who uses it, and how?
The revenue manager sees a daily cancellation risk score per booking in Tableau and uses it to decide how many extra rooms to sell.

## Cost of mistakes
- False negative (missed cancellation): We don't overbook against this booking, so the room may sit empty. Lost revenue is at most the value of the stay: roughly 285 (median rate of about 95 per night x median stay of 3 nights), or less if the room is resold.
- False positive (false alarm): We overbook expecting a cancellation, but the guest arrives. If the hotel is full, they must be moved elsewhere: replacement room, compensation, a bad review and possibly lost future business. This cost isn't in the dataset and needs an estimate from the revenue team.
- Which is worse? False positive. A missed cancellation costs a limited amount of revenue, while a false alarm can leave a real guest without a room and also damage the hotel's reputation. Since the goal is to overbook safely, we accept missing some cancellations to avoid this. Revisit once the revenue team has estimated the cost.

## Success metric
ROC-AUC on 2017 bookings, plus precision and recall at the threshold we pick. Set the threshold to keep precision high, because false positives are the costlier mistake.
Must beat the baseline (predict "no cancel" for everyone = 61.3% accuracy on 2017 bookings; 63.0% across all years).

## Known risks
- Leakage: columns filled in after the booking outcome (to check in Phase 3)