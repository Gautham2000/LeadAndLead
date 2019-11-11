import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapEventListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        # controller.enable_gesture(Leap.Gesture.Type.TYPE_SWIPE)
        controller.config.set("Gesture.Swipe.MinLength", 200.0)
        controller.config.save()

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_frame(self, controller):

    	left_bound = -50
    	right_bound = 50

    	up_bound = 360
    	down_bound = 220

    	back_bound = 120
    	forward_bound = -50

        frame = controller.frame()
        hand = frame.hands.rightmost
        position = hand.palm_position
        velocity = hand.palm_velocity
        direction = hand.direction
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)


	#Key-tap gesture
	for gesture in frame.gestures():
		if gesture.type is Leap.Gesture.TYPE_KEY_TAP:
			key_tap = Leap.KeyTapGesture(gesture)
			print ("Turning drone on")

		if gesture.type is Leap.Gesture.TYPE_CIRCLE:
			circle = Leap.CircleGesture(gesture)
			print("Turning off")


        for hand in frame.hands:

			handType = "Left hand" if hand.is_left else "Right hand"
			#print "  %s, id %d, position: %s" % (
   #          	handType, hand.id, hand.palm_position)

   			# print hand.palm_position
			#center point (0,200,0)		

			#x-axis	
			if (hand.palm_position[0] < left_bound):
				print ("Moving left")

			elif(hand.palm_position[0] > right_bound):
				print ("Moving right")

			#y-axis
			if (hand.palm_position[1] > up_bound):
				print ("Moving up")

			elif(hand.palm_position[1] < down_bound):
				print ("Moving down")


			#z-axis
			if (hand.palm_position[2] > back_bound):
				print ("Moving back")

			elif(hand.palm_position[2] < forward_bound):
				print ("Moving forward")

			if (hand.palm_position[0] > left_bound) and (hand.palm_position[0] < right_bound) and (hand.palm_position[1] < up_bound) and (hand.palm_position[1] > down_bound) and (hand.palm_position[2] < back_bound) and (hand.palm_position[2] > forward_bound):
				print "Not moving"



def main():

	listener = LeapEventListener()
	controller = Leap.Controller()
	controller.add_listener(listener)

	print "Press Enter to quit..."
   	try:
		sys.stdin.readline()
   	except KeyboardInterrupt:
		pass
   	finally:
        # Remove the sample listener when done
		controller.remove_listener(listener)

if __name__ == "__main__":
    main()