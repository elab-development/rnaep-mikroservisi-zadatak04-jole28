from database import redis

streams = ["order_completed", "refund_order"]

while True:
    messages = redis.xread({s: "$" for s in streams}, block=0)

    for stream, msgs in messages:
        for msg_id, data in msgs:

            if stream == "order_completed":
                print(f"Notification: Order {data['product_id']} completed")

            if stream == "refund_order":
                print(f"Notification: Order refunded {data['product_id']}")