class Solution(object):
	def haveConflict(self, event1, event2):
		start_time1, end_time1 = event1
		start_time2, end_time2 = event2

		# convert start and end time to minutes for comparison
		start_minutes1 = int(start_time1[:2]) * 60 + int(start_time1[3:])
		end_minutes1 = int(end_time1[:2]) * 60 + int(end_time1[3:])
		start_minutes2 = int(start_time2[:2]) * 60 + int(start_time2[3:])
		end_minutes2 = int(end_time2[:2]) * 60 + int(end_time2[3:])

		# check for overlap
		if start_minutes1 <= end_minutes2 and start_minutes2 <= end_minutes1:
			return True
		return False
