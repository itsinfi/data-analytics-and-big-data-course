def read_csv(csv_file: str, delimiter: str, eol: str, limit: int) -> list[dict[str, str]]:
    print(f'     --- Start reading f{csv_file}...');

    with open(csv_file, 'r') as file:
        try:
            lines = []
            for _ in range(limit + 1):
                lines.append(next(file).rstrip(eol));
        except StopIteration:
            pass;
        
        keys: list[str] = lines[0].split(delimiter);
        lines.pop(0);

        print(f'     --- Finish reading f{csv_file}...');
        return [dict(zip(keys, line.split(delimiter))) for line in lines];