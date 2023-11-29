STRING_TYPES = ['all', 'experimental', 'textmining']
HuRIs = ['HuRI','HI-union']
rule all:
    input:
        "work/string.all.txt",
        "work/string.textmining.txt",
        "work/string.experimental.txt",
        expand('work/Plots/string.{type}.degree_dists.png', type=STRING_TYPES),
        expand('work/Plots/{h_type}.degree_dists.png', h_type=HuRIs),

rule process_string_all:
    input:
        "String/9606.protein.links.detailed.v11.5.txt"
    output:
        "work/string.all.txt"
    shell:
        """
        cat {input} | cut -f1,2 -d' '  | grep -v protein1 | awk '{{print $1"\t"$2}}' > {output}
        """

rule process_string_experimental:
    input:
        "String/9606.protein.links.detailed.v11.5.txt"
    output:
        "work/string.experimental.txt"
    shell:
        """
        cat {input} | cut -f1,2,7 -d' ' | grep -v protein1 | awk '{{if ($3 > 0) print $1"\t"$2}}' > {output}
        """

rule process_string_textming:
    input:
        "String/9606.protein.links.detailed.v11.5.txt"
    output:
        "work/string.textmining.txt"
    shell:
        """
        cat {input} | cut -f1,2,9 -d' ' | grep -v protein1  | awk '{{if ($3 > 0) print $1"\t"$2}}' > {output}
        """

rule plot_degree_distributions:
    input:
        "work/string.{type}.txt",
    output:
        "work/Plots/string.{type}.degree_dists.png"
    shell:
        """
        mkdir -p work/Plots
        python Scripts/plot_edge_list.py {input}  {output}
        """

rule plot_degree_distributions_HuRI:
    input:
        "HuRI/{h_type}.tsv",
    output:
        'work/Plots/{h_type}.degree_dists.png'
    shell:
        """
        mkdir -p work/Plots
        python Scripts/plot_edge_list.py {input}  {output}
        """