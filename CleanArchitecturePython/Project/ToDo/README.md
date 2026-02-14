```bash
project_root/
├── core/
│   ├── entities/
│   │   ├── task.py
│   │   ├── assignee.py
│   │   └── repository.py   
│   │
│   ├── interface
│   │   ├── api/
│   │   │   └── task_router.py
│   │   └── cli/
│   │       └── task_handler.py
│   │
│   ├── usecases/
│   │   └── task_usecase.py
│   │
│   └── infrastructure/
│       └── persistence/
│           └── file_repository.py
│   
├── entrypoints/
│   ├── api_main.py
│   ├── cli_main.py
│   └── bot_main.py
├── env
├── README.md
├── requirements.txt
└── tasks.json 

```

```mermaid
graph TD
    A[entrypoints FastAPI / CLI] -->|calls| B[usecases TaskUseCase]
    B -->|uses via interface| C[entities TaskRepository Interface]
    C -->|implemented by| D[infra.persistence.FileTaskRepository]

    subgraph EntryPoints
        A1[create_task]
        A2[update_task]
        A3[delete_task]
        A4[list_tasks]
    end

    subgraph UseCase Layer
        B1[TaskUseCase.create]
        B2[TaskUseCase.update]
        B3[TaskUseCase.delete]
        B4[TaskUseCase.list]
    end

    subgraph Entity Layer
        C1[TaskRepository ABC]
    end

    subgraph Infrastructure Layer
        D1[FileTaskRepository]
        D1 -->|reads/writes| E[tasks.json]
    end

    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4

    B1 --> C1
    B2 --> C1
    B3 --> C1
    B4 --> C1

    C1 --> D1
```



# Cli

`create-task`
```bash
python entrypoints/cli_main.py create-task \
  --title "اولیه" --description "تسک تست"
```



```bash
python entrypoints/cli_main.py create-task \
  --title "تحلیل بازار" \
  --description "تحلیل تکنیکال در اکسل" \
  --assignee-id 5 \
  --assignee-name "علی اکبری" \
  --assignee-email "ali@example.com"
```
---

`update-task`
```bash
python entrypoints/cli_main.py update-task \
  --id 1 \
  --title "ویرایش‌شده" \
  --description "توضیح جدید" \
  --assignee-id 10 \
  --assignee-name "محمدی" \
  --assignee-email "mohammadi@example.com"
```

---
`update-task`

```bash
python3 entrypoints/cli_main.py list-tasks
```


# api
`Address`

>> http://127.0.0.1:8000/docs

```json
{
  "title": "تحویل فاز اول",
  "description": "مربوط به طراحی لایه usecase",
  "assignee": {
    "id": 4,
    "name": "رضا پژوهنده",
    "email": "reza@domain.com"
  }
}

```