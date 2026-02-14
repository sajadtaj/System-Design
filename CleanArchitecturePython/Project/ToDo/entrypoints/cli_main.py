# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import argparse
from core.interfaces.cli.task_handler import TaskHandler
from core.usecases.task_usecase import TaskUseCase
from core.infrastructure.persistence.file_repository import FileTaskRepository 

def main():
    parser = argparse.ArgumentParser(description="ToDo CLI")

    subparsers = parser.add_subparsers(dest='command')

    # Create Task
    create_parser = subparsers.add_parser("create-task", help="ایجاد تسک جدید")
    create_parser.add_argument("--title", required=True, help="عنوان تسک")
    create_parser.add_argument("--description", required=True, help="توضیحات تسک")
    create_parser.add_argument("--assignee-id", type=int, help="ID مسئول تسک")
    create_parser.add_argument("--assignee-name", type=str, help="نام مسئول")
    create_parser.add_argument("--assignee-email", type=str, help="ایمیل مسئول")
    
    # List Tasks
    list_parser = subparsers.add_parser("list-tasks", help="نمایش همه تسک‌ها")
    
    delete_parser = subparsers.add_parser("delete-task", help="حذف تسک") 
    delete_parser.add_argument("--id", required=True, type=int, help="شناسه تسک برای حذف")



    # Update Task
    update_parser = subparsers.add_parser("update-task", help="ویرایش تسک موجود")
    update_parser.add_argument("--id", type=int, required=True, help="شناسه تسک")
    update_parser.add_argument("--title", required=True, help="عنوان جدید")
    update_parser.add_argument("--description", required=True, help="توضیح جدید")
    update_parser.add_argument("--assignee-id", type=int, help="شناسه مسئول جدید")
    update_parser.add_argument("--assignee-name", type=str, help="نام مسئول جدید")
    update_parser.add_argument("--assignee-email", type=str, help="ایمیل مسئول جدید")

    args = parser.parse_args()

    # وابستگی‌ها
    repo = FileTaskRepository("tasks.json")  
    usecase = TaskUseCase(repo)
    handler = TaskHandler(usecase)

    if args.command == "create-task":
        handler.create_task(
            title=args.title,
            description=args.description,
            assignee_id=args.assignee_id,
            assignee_name=args.assignee_name,
            assignee_email=args.assignee_email
        )
    elif args.command == "list-tasks":
        handler.list_tasks()

    elif args.command == "delete-task":
        handler.delete_task(args.id)

    elif args.command == "update-task":
        handler.update_task(
            task_id=args.id,
            title=args.title,
            description=args.description,
            assignee_id=args.assignee_id,
            assignee_name=args.assignee_name,
            assignee_email=args.assignee_email
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
