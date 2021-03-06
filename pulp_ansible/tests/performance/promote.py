import argparse

import django  # noqa otherwise E402: module level not at top of file

django.setup()  # noqa otherwise E402: module level not at top of file

from pulpcore.plugin.tasking import enqueue_with_reservation

from pulp_ansible.app.tasks.test_tasks import promote_content


parser = argparse.ArgumentParser(description="Find a collection and promote it.")

parser.add_argument(
    "--repos-per-task",
    metavar="PATH",
    type=int,
    nargs=1,
    required=True,
    help="The number of repositories each task should handle.",
)
parser.add_argument(
    "--num-repos-to-update",
    metavar="PATH",
    type=int,
    nargs=1,
    required=True,
    help="The number of repositories to have this content added to.",
)

args = parser.parse_args()


if __name__ == "__main__":
    task_args = (args.repos_per_task[0], args.num_repos_to_update[0])
    enqueue_with_reservation(promote_content, [], args=task_args)
