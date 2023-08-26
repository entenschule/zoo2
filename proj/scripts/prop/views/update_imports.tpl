class {{class_name}}Properties:

    % for name in names:
    from .{{name}} import {{name}}
    % end
