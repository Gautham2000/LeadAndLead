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

        frame = controller.frame()
        hand = frame.hands.rightmost
        position = hand.palm_position
        velocity = hand.palm_velocity
        direction = hand.direction

        for hand in frame.hands:

			handType = "Left hand" if hand.is_left else "Right hand"
			#print "  %s, id %d, position: %s" % (
   #          	handType, hand.id, hand.palm_position)


			
			if (hand.palm_position[0] < -30):
				print ("Moving left")

			elif(hand.palm_position[0] > 30):
				print ("Moving right")

			if (hand.palm_position[1] > 170):
				print ("Moving up")

			elif(hand.palm_position[1] < 100):
				print ("Moving down")


			if (hand.palm_position[2] > 50):
				print ("Moving back")

			elif(hand.palm_position[2] < -50):
				print ("Moving forward")

			else:
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