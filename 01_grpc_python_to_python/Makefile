.PHONY: test run proto

proto:
	@bash -c "chmod +x ./scripts/genenrate_pb.sh"
	@bash -c "./scripts/genenrate_pb.sh"

test:
	pytest python/tests/test_server.py;

run: proto
	@bash -c "docker-compose up"
