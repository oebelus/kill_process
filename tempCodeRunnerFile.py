process.kill()
                        print(f'Process {process.name()} was killed')
                    except psutil.AccessDenied:
                        prin