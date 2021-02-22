import argparse
import read_xls
import gitlab_handler


def parse_args():
    parser = argparse.ArgumentParser(description='Process member.xls')
    parser.add_argument(
        '--xls',
        dest='xls_path',
        help='the path of member.xls',
        required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    students = read_xls.get_students_from_ilms_member_xls(args.xls_path)

    for s in students:
        gitlab_handler.create_user(s.get_query_for_creation())


if __name__ == "__main__":
    main()
