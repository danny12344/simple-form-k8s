#!/bin/sh

# Start the application
uvicorn main:app --host 0.0.0.0 --port 8080

# Log any errors that occur
RETVAL=$?
if [ $RETVAL -ne 0 ]; then
  echo "Error occurred during container startup. Exit code: $RETVAL" >> error.log
fi

# Exit with the proper status code
exit $RETVAL
